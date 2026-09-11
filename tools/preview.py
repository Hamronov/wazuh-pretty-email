#!/usr/bin/env python3
"""Render the bundled synthetic alert locally without sending email."""
import json
from pathlib import Path
import runpy
import sys

ROOT = Path(__file__).resolve().parents[1]


def main():
    output = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / 'preview'
    output.mkdir(parents=True, exist_ok=True)
    config_path = ROOT / 'config/custom_pretty_email.example.json'
    cfg = json.loads(config_path.read_text(encoding='utf-8'))
    alert = json.loads((ROOT / 'examples/alert.json').read_text(encoding='utf-8'))
    module = runpy.run_path(str(ROOT / 'integrations/custom-pretty-email'),
                            run_name='preview_only')
    globals_ = module['get_alert_meta'].__globals__
    globals_['CONFIG_PATH'] = str(config_path)

    def refuse_smtp(*args, **kwargs):
        raise RuntimeError('SMTP is disabled in the offline preview')

    globals_['send_email'] = refuse_smtp
    subject, text, html = module['build_messages'](module['get_alert_meta'](alert), cfg)
    (output / 'email.html').write_text(html, encoding='utf-8')
    (output / 'email.txt').write_text(subject + '\n\n' + text, encoding='utf-8')
    print(f'Offline preview: {output.resolve() / "email.html"}')


if __name__ == '__main__':
    main()
