import argparse
from Exploitation import http_pollution, sqlinjection, command_inj, xmleei, htmli, frame_inj


def main():
    parser = argparse.ArgumentParser(description="Porównuje dwie strony HTML.")
    parser.add_argument("--url", type=str, help="Adres URL strony (wraz z parametrem jeżeli http_polution)")
    parser.add_argument("--http-polution", action="store_true", help="HTTP polution")
    parser.add_argument(
        "--parameter", nargs="*", type=str, help='Podaj parametry GET po spacjach w ""'
    )
    # parser.add_argument('--xssget', action='store_true', help='XSS via GET')
    # parser.add_argument('--xsspost', action='store_true', help='XSS via POST')
    parser.add_argument(
        "--sqli",
        type=str,
        nargs="?",
        const="Normal",
        help='SQLI via POST: currently supported: "Normal", "Insert", "Timing"',
    )
    parser.add_argument(
        "--comminj",
        type=str,
        nargs="?",
        const="AND",
        help='Command Injection: currently supporte: "AND", "DoubleAND", "OR"',
    )
    parser.add_argument(
        "--xmleei", action="store_true", help="XML External Entity Injection"
    )
    parser.add_argument(
        "--htmli",
        type=str,
        nargs="?",
        const="Onsite",
        help='HTML Injection currently supported: "Onsite", "Header", "Cookie"',
    )
    parser.add_argument("--autoforms", action="store_true", help="Scrap all forms")
    parser.add_argument("--postdata", nargs="*", help="Post Data")
    args = parser.parse_args()

    if args.http_polution:
        print(http_pollution(args.url, args.parameter))
    # elif args.xssget:
    #     print(xss_get(args.url))
    # elif args.xsspost:
    #     print(xss_post(args.url, args.autoforms, args.postdata))
    elif args.sqli:
        print(sqlinjection(args.url, args.sqli, args.autoforms, args.postdata))
    elif args.comminj:
        print(command_inj(args.url, args.comminj, args.autoforms, args.postdata))
    elif args.xmleei:
        print(xmleei(args.url, args.autoforms, args.postdata))
    elif args.htmli:
        print(htmli(args.url, args.htmli, args.autoforms))
    else:
        print("Nie podano odpowiedniego argumentu.")


if __name__ == "__main__":
    main()
