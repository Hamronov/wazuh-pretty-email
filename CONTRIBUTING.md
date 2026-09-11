# Contributing

Thank you for helping improve Wazuh Pretty Email. Bug reports, documentation improvements, and pull requests are welcome.

## Report a bug

Open an issue describing expected and actual behavior, your Wazuh and Python versions, and the relevant error. Include a minimal synthetic alert where possible. Remove credentials, real recipients, internal addresses, hostnames, usernames, and other sensitive event content before posting.

Do not publish sensitive vulnerability details in an ordinary issue. Use GitHub's private vulnerability reporting option if enabled; otherwise request a private contact channel without posting exploit details or confidential data.

## Submit changes

1. Fork the repository and create a focused branch.
2. Make the change and update the relevant documentation and examples.
3. Run `python3 tools/preview.py` on Linux or macOS.
4. For behavior changes, add or run focused checks covering affected filtering, state, or rendering behavior. Mock SMTP; do not send mail as part of an automated test.
5. Review the diff for production data and credentials.
6. Open a pull request explaining the problem, resulting behavior, and validation performed.

The integration currently uses Python's standard library. Explain any proposed new dependency and its deployment impact. Keep alert thresholds, exclusions, and delivery semantics explicit in changes.

The offline preview is a rendering check, not an end-to-end delivery test. Clearly distinguish local verification from tests on a real Wazuh Manager.

## License

Submit only code and materials you have the right to contribute. Contributions to this project are intended to be distributed under its MIT license. Keep existing copyright and license notices. You retain copyright in your own contributions; no copyright assignment is requested.
