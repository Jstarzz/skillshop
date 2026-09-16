#!/usr/bin/env python3
import json
import os
import re
import sys
from pathlib import Path


def looks_like_project(cwd: str) -> bool:
    root = Path(cwd or os.getcwd())
    markers = (
        ".git", "package.json", "pnpm-lock.yaml", "yarn.lock", "bun.lockb",
        "pyproject.toml", "requirements.txt", "go.mod", "Cargo.toml",
        "composer.json", "Gemfile", "pom.xml", "build.gradle", "build.gradle.kts",
        "Dockerfile", "docker-compose.yml", "compose.yml", "Makefile",
    )
    if any((root / marker).exists() for marker in markers):
        return True
    try:
        if any(root.glob("*.sln")) or any(root.glob("*.csproj")):
            return True
    except OSError:
        pass
    return any((root / d).is_dir() for d in ("src", "app", "apps", "packages", "server", "client", "api"))


def obvious_chitchat(prompt: str) -> bool:
    text = re.sub(r"\s+", " ", prompt.strip().lower())
    words = text.split()
    if len(words) > 14:
        return False
    if text in {"thanks", "thank you", "ty", "ok", "okay", "cool", "nice", "lol", "lmao", "got it", "perfect"}:
        return True
    return bool(re.match(r"^(hi|hello|hey|yo|good morning|good afternoon|good evening|good night)\b", text))


def engineering_signal(prompt: str) -> bool:
    text = prompt.lower()
    terms = (
        "code", "repo", "repository", "project", "bug", "fix", "implement", "feature",
        "refactor", "review", "production", "deploy", "release", "api", "endpoint",
        "database", "sql", "migration", "schema", "backend", "frontend", "ui", "ux",
        "test", "qa", "playwright", "security", "auth", "payment", "performance",
        "load test", "benchmark", "latency", "throughput", "memory", "cpu", "docker",
        "kubernetes", "server", "infra", "ci", "github actions", "typescript", "javascript",
        "python", "php", "react", "astro", "go ", "rust", "c#", ".net", "java",
        "architecture", "design this system", "debug", "error", "exception", "build",
        "dependency", "package", "npm", "pnpm", "git", "branch", "pull request", "pr ",
        "mobile app", "android", "ios", "nfc", "webhook", "cache", "redis", "queue",
        "component", "design system", "webgl", "three.js", "threejs", "threeui",
    )
    return any(term in text for term in terms)


def project_action_signal(prompt: str) -> bool:
    """Catch implicit repo edits without treating the current directory as user intent."""
    text = re.sub(r"\s+", " ", prompt.strip().lower())
    actions = (
        "add", "change", "update", "remove", "delete", "rename", "create", "implement",
        "fix", "debug", "refactor", "optimize", "review", "audit", "inspect", "trace",
        "test", "verify", "benchmark", "profile", "ship", "deploy", "build", "wire", "connect",
    )
    targets = (
        "this", "that", "it", "file", "function", "class", "component", "page", "screen",
        "route", "endpoint", "service", "server", "client", "app", "repo", "project", "code",
        "config", "workflow", "script", "package", "dependency", "database", "schema",
    )
    return any(re.search(rf"\b{re.escape(action)}\b", text) for action in actions) and any(
        re.search(rf"\b{re.escape(target)}\b", text) for target in targets
    )


def main() -> None:
    try:
        data = json.load(sys.stdin)
    except Exception:
        return

    prompt = str(data.get("prompt") or "").strip()
    if not prompt or prompt.startswith("/") or obvious_chitchat(prompt):
        return

    cwd = str(data.get("cwd") or os.getcwd())
    should_route = engineering_signal(prompt) or (looks_like_project(cwd) and project_action_signal(prompt))
    if not should_route:
        return

    context = (
        "SkillShop: substantive engineering intent detected. Invoke `skillshop:shop` before the work "
        "and load only the smallest useful playbook set. Ignore this if the turn is actually trivial."
    )
    print(json.dumps({
        "hookSpecificOutput": {
            "hookEventName": "UserPromptSubmit",
            "additionalContext": context,
        }
    }))


if __name__ == "__main__":
    main()
