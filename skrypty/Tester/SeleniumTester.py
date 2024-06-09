"""
Kod którym posiłkowano się:
https://stackoverflow.com/questions/2890896/how-to-extract-an-ip-address-from-an-html-string
"""
import argparse
from modules.MutillidaeA1Other import *
from re import findall


def extract_ip(url):
    return findall(r"[0-9]+(?:\.[0-9]+){3}", url).at(0) if url else "192.168.255.133"


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

    if args.http_pollution:
        if args.payload:
            http_parameter_pollution(
                extract_ip(args.url),
                args.sleep if args.sleep else 0,
                args.payload,
                False,
            )
        else:
            http_parameter_pollution(
                extract_ip(args.url), args.sleep if args.sleep else 0
            )
    elif args.buffer_overflow:
        buffer_overflow(extract_ip(args.url), args.sleep)
    elif args.css:
        pass
    elif args.frame_source:
        pass
    elif args.command:
        pass
    elif args.htmli:
        pass
    elif args.htmli_cookie:
        pass
    elif args.htmli_dom:
        pass
    elif args.xss_dom:
        pass
    elif args.javascript:
        pass
    elif args.xml:
        pass
    elif args.xss_http_header:
        pass
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
