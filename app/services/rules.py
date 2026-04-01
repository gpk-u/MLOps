def rule_engine(text: str):

    # latency
    if "response time" in text or "latency" in text:
        return "Latency"

    # cpu
    if "cpu" in text:
        return "CPU"

    # memory
    if "memory" in text:
        return "Memory"

    # error rate
    if "error" in text or "5xx" in text or "4xx" in text:
        return "Error Rate"

    # disk
    if "disk" in text or "ebs" in text or "volume" in text:
        return "Disk Space"

    # service request
    if "create" in text or "access" in text or "vpn" in text:
        return "SR"
    
    # IAM
    if "policy" in text or "role" in text or "iam" in text:
        return "IAM"
    
    # CDN
    if "cloudfront" in text or "distribution" in text or "frontdoor" in text:
        return "CDN"

    return None