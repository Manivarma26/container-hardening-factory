#!/usr/bin/env python3
import os, sys, yaml, json

def load_yaml(file_path):
    with open(file_path, "r") as f:
        return yaml.safe_load(f)

def validate_base_images(policy):
    approved = policy.get("approved_base_images", [])
    disallowed = policy.get("disallowed_images", [])
    if not approved:
        print("❌ No approved base images defined!")
        return False
    print(f"✅ Found {len(approved)} approved base images.")
    print(f"🚫 {len(disallowed)} disallowed base images listed.")
    return True

def validate_cve_thresholds(policy):
    if policy.get("allow_critical", 0) != 0:
        print("❌ Policy violation: Critical CVEs allowed > 0.")
        return False
    print("✅ CVE threshold policy validated successfully.")
    return True

def validate_docker_bench(policy):
    mandatory = ["no_root_user", "healthcheck_defined", "capabilities_dropped"]
    for rule in mandatory:
        if rule not in policy["rules"] or not policy["rules"][rule]:
            print(f"❌ Missing or disabled mandatory rule: {rule}")
            return False
    print("✅ Docker benchmark rules validated successfully.")
    return True

if __name__ == "__main__":
    base_dir = "policies"
    base_policy = load_yaml(os.path.join(base_dir, "base-image-whitelist.yml"))
    cve_policy = load_yaml(os.path.join(base_dir, "cve-thresholds.yml"))
    docker_policy = load_yaml(os.path.join(base_dir, "docker-benchmark.yml"))

    results = [
        validate_base_images(base_policy),
        validate_cve_thresholds(cve_policy),
        validate_docker_bench(docker_policy)
    ]

    if not all(results):
        print("\n❌ Container policy validation failed. Please review violations.")
        sys.exit(1)
    else:
        print("\n✅ All container governance policies validated successfully.")
