import re

def check_hash_validity(hash_str):
    hash_str = hash_str.strip().lower()
    patterns = {
        "MD5": r"^[a-f0-9]{32}$",
        "SHA1": r"^[a-f0-9]{40}$",
        "SHA256": r"^[a-f0-9]{64}$",
        "SHA512": r"^[a-f0-9]{128}$"
    }
    for algo, pattern in patterns.items():
        if re.fullmatch(pattern, hash_str):
            print(f"Valid {algo} hash.\n")
            return True
    print("Invalid or unknown hash format.\n")
    return False

def check_legality_info():
    print("=======================================")
    print("Smart Contract Legality Checker")
    print("=======================================")

    contract_type = input("Contract type (e.g., Token, NFT, Crowdfunding, Lottery): ").strip().lower()
    features = input("List contract features (comma-separated, e.g., burn, blacklist, selfdestruct): ").strip().lower()
    kyc_required = input("Is KYC/AML required? (yes/no): ").strip().lower()
    jurisdiction = input("Jurisdiction (Country or State): ").strip().lower()
    centralized = input("Is the contract controlled by an owner/admin? (yes/no): ").strip().lower()

    illegal_flags = []
    warning_flags = []

    if contract_type in ["lottery", "gambling", "betting"]:
        illegal_flags.append("Gambling/lottery contracts may be illegal without a valid license.")
    if "ponzi" in features or "pyramid" in features:
        illegal_flags.append("Ponzi/pyramid schemes are banned in most jurisdictions.")
    if "selfdestruct" in features:
        warning_flags.append("Uses 'selfdestruct' — often found in scam contracts.")
    if "blacklist" in features and centralized == "yes":
        warning_flags.append("Central admin + blacklist may violate decentralization claims.")
    if kyc_required == "yes" and centralized == "no":
        warning_flags.append("KYC requires authority — mismatch with decentralization.")
    if contract_type == "token":
        if centralized == "yes" and kyc_required == "no":
            warning_flags.append("Centralized token with no KYC can raise legal risks.")
    if "india" in jurisdiction:
        if contract_type in ["lottery", "gambling", "betting"]:
            illegal_flags.append("Gambling/lottery is banned/restricted in India.")
        if contract_type == "token" and centralized == "yes":
            warning_flags.append("SEBI regulation may apply to centralized tokens.")

    print("\n=======================================")
    print("LEGALITY REPORT")
    print("=======================================")

    if illegal_flags or warning_flags:
        for flag in illegal_flags:
            print(flag)
        for flag in warning_flags:
            print(flag)
    else:
        print("No major legal red flags based on your inputs.")

    print("\nDISCLAIMER:")
    print("This is a basic rule-based tool. Consult a legal expert for full guidance.")

def main():
    print("=======================================")
    print("Enter a Hash to Begin")
    print("=======================================")

    hash_input = input("Paste your hash: ")
    if check_hash_validity(hash_input):
        next_step = input("Continue to Smart Contract Legality Checker? (yes/no): ").strip().lower()
        if next_step == "yes":
            check_legality_info()
        else:
            print("Done. Exited after hash check.")
    else:
        print("Invalid hash. Exiting.")

if __name__ == "__main__":
    main()
