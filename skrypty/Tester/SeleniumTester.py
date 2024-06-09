"""
Kod którym posiłkowano się:
https://stackoverflow.com/questions/2890896/how-to-extract-an-ip-address-from-an-html-string
"""
import argparse
from modules.MutillidaeA1Other import *
from re import findall


def extract_ip(url):
    return findall(r"[0-9]+(?:\.[0-9]+){3}", url)[0] if url else "192.168.255.133"


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
    # parser.add_argument("--xssget", action="store_true", help="XSS via GET")
    # parser.add_argument("--xsspost", action="store_true", help="XSS via POST")
    # parser.add_argument(
    #     "--sqli",
    #     type=str,
    #     nargs="?",
    #     const="Normal",
    #     help='SQLI via POST: currently supported: "Normal", "Insert", "Timing"',
    # )
    # parser.add_argument("--postdata", nargs="*", help="Post Data")
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
    }

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
    # elif args.xssget:
    #     print(xss_get(args.url))
    # elif args.xsspost:
    #     print(xss_post(args.url, args.postdata))
    # elif args.sqli:
    #     print(sqlinjection(args.url, args.sqli, args.postdata))
    else:
        print("Nie podano odpowiedniego argumentu.")


if __name__ == "__main__":
    main()
