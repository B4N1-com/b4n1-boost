# git hooks — b4n1-boost public mirror

Versioned hooks; git does NOT auto-apply them on clone. Activate locally:

```bash
git config core.hooksPath .githooks
```

| Hook | What it enforces |
|---|---|
| `commit-msg` | No AI-attribution lines (Co-Authored-By / generated-with) in commit messages — AGENTS.md §10g. |
| `pre-push` | Block publishing private material to the public storefront (§10h/§10m): Rust source/manifests (`*.rs`, `Cargo.toml/lock`, `*.ld`), env/credential files (`.env*`, `.npmrc`, `.pypirc`, `.netrc`), key material (`*.pem`, `*.key`, `id_*`, `*.p12`), private-key blocks or registry-token assignments inside outgoing diffs, and pushes to a non-canonical remote. Exit 0 clean · 1 leak · 2 internal error. |

Extra push destinations (e.g. a second mirror) must be authorized once per clone:

```bash
git config --local --add b4n1.mirrorPushAllow '<regexp matching its url>'
```

The registered suite pins this hook's behavior: `bash cli.sh test b4n1-boost`
(section "mirror pre-push guard") drives the real script against a scratch
clone with a leaked commit and with a clean one.
