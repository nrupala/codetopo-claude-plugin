"""Validation suite for the codetopo Claude plugin package.

This repository is a plugin/marketplace package: JSON manifests, a skill
document, and a pre-built MCPB bundle — there is no compiled code. The suite
validates the package the way a consumer's installer would read it:

- every JSON manifest parses and carries its required fields;
- every file a manifest references actually exists in the repo;
- the version declared in the plugin manifest agrees with the shipped
  bundle filename and with what the README tells users to download;
- the bundled skill's frontmatter names the same plugin.

Run from the repository root:  python3 -m unittest discover -s tests
"""

import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PLUGIN_JSON = ROOT / ".claude-plugin" / "plugin.json"
SEMVER = re.compile(r"^\d+\.\d+\.\d+$")


def load_json(path):
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


class PluginManifestTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.plugin = load_json(PLUGIN_JSON)

    def test_plugin_json_parses_and_has_required_fields(self):
        for field in ("name", "version", "description", "author", "license"):
            self.assertIn(field, self.plugin, f"plugin.json missing {field!r}")
            self.assertTrue(self.plugin[field], f"plugin.json {field!r} is empty")

    def test_version_is_semver(self):
        self.assertRegex(self.plugin["version"], SEMVER)

    def test_license_field_matches_license_file(self):
        license_file = ROOT / "LICENSE"
        self.assertTrue(license_file.is_file(), "LICENSE file missing")
        self.assertGreater(license_file.stat().st_size, 1000)
        # plugin.json declares AGPL-3.0-or-later; the LICENSE text is the AGPL.
        self.assertTrue(self.plugin["license"].startswith("AGPL"))
        self.assertIn("GNU AFFERO GENERAL PUBLIC LICENSE",
                      license_file.read_text(encoding="utf-8"))

    def test_mcp_servers_reference_resolves(self):
        ref = self.plugin.get("mcpServers")
        self.assertIsInstance(ref, str, "plugin.json mcpServers must be a path")
        mcp_path = (ROOT / ref).resolve()
        self.assertTrue(mcp_path.is_file(), f"referenced MCP file missing: {ref}")
        mcp = load_json(mcp_path)
        servers = mcp.get("mcpServers")
        self.assertIsInstance(servers, dict)
        self.assertIn(self.plugin["name"], servers,
                      "MCP server name must match the plugin name")
        server = servers[self.plugin["name"]]
        self.assertIsInstance(server.get("command"), str)
        self.assertTrue(server["command"], "MCP server command is empty")
        self.assertIsInstance(server.get("args"), list)

    def test_version_consistent_with_bundle_and_readme(self):
        version = self.plugin["version"]
        bundle = ROOT / f"codetopo-{version}.mcpb"
        self.assertTrue(bundle.is_file(),
                        f"bundle for declared version missing: {bundle.name}")
        self.assertGreater(bundle.stat().st_size, 1000, "bundle looks empty")
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn(f"codetopo-{version}.mcpb", readme,
                      "README download instructions name a different bundle")

    def test_skill_file_matches_plugin(self):
        skill = ROOT / "skills" / self.plugin["name"] / "SKILL.md"
        self.assertTrue(skill.is_file(), f"skill file missing: {skill}")
        text = skill.read_text(encoding="utf-8")
        self.assertTrue(text.startswith("---"), "SKILL.md lacks frontmatter")
        frontmatter = text.split("---", 2)[1]
        self.assertIn(f"name: {self.plugin['name']}", frontmatter)
        self.assertIn("description:", frontmatter)


if __name__ == "__main__":
    unittest.main()
