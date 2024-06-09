import argparse
from Exploitation import http_pollution, xss_get, xss_post, sqlinjection, test_options


def main():
    parser = argparse.ArgumentParser(
        description="Testuje podatności za pomocą selenium."
    )
    parser.add_argument("--url", type=str, help="Adres URL strony wraz z parametrem")
    parser.add_argument("--http-polution", action="store_true", help="HTTP polution")
    parser.add_argument("--xssget", action="store_true", help="XSS via GET")
    parser.add_argument("--xsspost", action="store_true", help="XSS via POST")
    parser.add_argument(
        "--sqli",
        type=str,
        nargs="?",
        const="Normal",
        help='SQLI via POST: currently supported: "Normal", "Insert", "Timing"',
    )
    parser.add_argument("--postdata", nargs="*", help="Post Data")
    args = parser.parse_args()

    if args.http_polution:
        print(http_pollution(args.url))
    elif args.xssget:
        print(xss_get(args.url))
    elif args.xsspost:
        print(xss_post(args.url, args.postdata))
    elif args.sqli:
        print(sqlinjection(args.url, args.sqli, args.postdata))
    else:
        print("Nie podano odpowiedniego argumentu.")
        print(test_options(args.url))


if __name__ == "__main__":
    main()
