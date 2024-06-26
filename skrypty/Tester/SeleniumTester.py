"""
Kod którym posiłkowano się:
https://stackoverflow.com/questions/2890896/how-to-extract-an-ip-address-from-an-html-string
"""

import argparse
from modules.MutillidaeA1Other import *
from modules.MutillidaeA1Sqli import *
from modules.MutillidaeA2BrokenAuthentication import *
from modules.MutillidaeA3XSS import *
from modules.MutillidaeA4IDOR import *
from re import findall
from os import path
from json import load


def extract_ip(url):
    if url:
        if findall(r"[0-9]+(?:\.[0-9]+){3}:[0-9]+", url):
            return findall(r"[0-9]+(?:\.[0-9]+){3}:[0-9]+", url)[0]
        elif findall(r"(?<=:\/\/)(.*?)(?=\/mutillidae)", url):
            return findall(r"(?<=:\/\/)(.*?)(?=\/mutillidae)", url)[0]
        elif findall(r"https?://([^/]+)", url):
            return findall(r"https?://([^/]+)", url)[0]
    config_file_path = "config.json"
    if path.exists(config_file_path):
        with open(config_file_path, "r") as config_file:
            config = load(config_file)
            if "server_ip" in config:
                return config.get("server_ip")
    return None


def main():
    parser = argparse.ArgumentParser(
        description="Testuje podatności za pomocą selenium."
    )
    parser.add_argument(
        "--url", type=str, help="Adres URL strony z adresem ip lub adres ip"
    )
    parser.add_argument(
        "--payload", type=str, help="Payload wstrzykiwany w wybranym rodzaju ataku"
    )
    parser.add_argument(
        "--sleep",
        type=int,
        help="Czas (w sekundach) od wykonania payloadu do zamknięcia przeglądarki",
    )
    parser.add_argument(
        "--buffer-overflow", action="store_true", help="Buffer overflow"
    )
    parser.add_argument(
        "--http-pollution", action="store_true", help="HTTP parameter polution"
    )
    parser.add_argument("--css", action="store_true", help="CSS injection")
    parser.add_argument(
        "--frame-source", action="store_true", help="Frame source injection"
    )
    parser.add_argument("--command", action="store_true", help="Command injection")
    parser.add_argument("--htmli", action="store_true", help="HTML injection")
    parser.add_argument(
        "--htmli-cookie", action="store_true", help="HTML via cookie injection"
    )
    parser.add_argument(
        "--htmli-dom", action="store_true", help="HTML via DOM injection"
    )
    parser.add_argument("--xss-dom", action="store_true", help="XSS via DOM injection")
    parser.add_argument(
        "--javascript", action="store_true", help="Javascript injection"
    )
    parser.add_argument(
        "--xml", action="store_true", help="XML external entity injection"
    )
    parser.add_argument(
        "--xss-http-header", action="store_true", help="XSS via DOM injection"
    )
    parser.add_argument(
        "--blind-sqli", action="store_true", help="BLIND SQL injection via timing"
    )
    parser.add_argument(
        "--sqli-bypass-auth",
        action="store_true",
        help="SQL injection - bypass authentication",
    )
    parser.add_argument(
        "--sqli-extract-data", action="store_true", help="SQL injection - extract data"
    )
    parser.add_argument(
        "--sqli-insert",
        action="store_true",
        help="SQL injection - INSERT injection into password input at register form. Tip for custom injections: Login password is set to x",
    )
    parser.add_argument(
        "--priv-esc",
        action="store_true",
        help="Privilege escalation via cookie injection",
    )
    parser.add_argument(
        "--idor",
        action="store_true",
        help="Insecure Direct Object References - Text File Viewer",
    )
    parser.add_argument(
        "--xss-persistent", action="store_true", help="XSS Persistent (Second Order)"
    )
    parser.add_argument(
        "--xss-reflected-1", action="store_true", help="Reflected (First Order)"
    )
    parser.add_argument(
        "--xss-reflected-2",
        action="store_true",
        help="Reflected (First order) - Set Background colour",
    )
    parser.add_argument(
        "--xss-via-html-attribute", action="store_true", help="XSS Via HTML Attribute"
    )
    parser.add_argument(
        "--xss-against-json", action="store_true", help="XSS Against JSON"
    )
    parser.add_argument(
        "--xss-via-http-headers", action="store_true", help="XSS via HTTP headers"
    )

    args = parser.parse_args()
    flag_to_function = {
        "http_pollution": http_parameter_pollution,
        "css": css_injection,
        "frame_source": frame_source_injection,
        "command": command_injection,
        "htmli": html_injection,
        "htmli_cookie": html_injection_via_cookie_into_phpsessid,
        "htmli_dom": html_injection_via_dom_injection,
        "xss_dom": xss_injection_via_dom_injection,
        "javascript": javascript_injection,
        "xml": xml_external_entity_injection,
        "xss_http_header": xss_injection_via_http_header,
        "blind_sqli": blind_sqli_via_timing,
        "sqli_bypass_auth": sqli_bypass_authentication,
        "sqli_extract_data": sqli_extract_data,
        "sqli_insert": sqli_insert,
        "priv_esc": privilege_escalation_via_cookie_into_uid,
        "idor": idor,
        "xss_persistent": xss_persistent,
        "xss_reflected_1": xss_reflected_1,
        "xss_reflected_2": xss_reflected_2,
        "xss_via_html_attribute": xss_via_html_attribute,
        "xss_against_json": xss_against_json,
        "xss_via_http_headers": xss_via_http_headers,
    }

    if extract_ip(args.url) is None:
        print("No url provided nor correct config file")
        return
    for flag, function in flag_to_function.items():
        if getattr(args, flag):
            if args.payload:
                function(
                    extract_ip(args.url),
                    args.sleep if args.sleep else 0,
                    args.payload,
                    False,
                )
                return
            else:
                function(extract_ip(args.url), args.sleep if args.sleep else 0)
                return
    if args.buffer_overflow:
        buffer_overflow(extract_ip(args.url), args.sleep if args.sleep else 0)
    else:
        print("Nie podano odpowiedniego argumentu.")


if __name__ == "__main__":
    main()
