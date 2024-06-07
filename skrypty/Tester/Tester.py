import argparse
from Exploitation import http_pollution, xss_get, xss_post, sqlinjection

def main():
    parser = argparse.ArgumentParser(description='Porównuje dwie strony HTML.')
    parser.add_argument('--url', type=str, help='Adres URL strony wraz z parametrem')
    parser.add_argument('--parameter', nargs='*', type=str, help='Podaj parametry po ","')
    parser.add_argument('--autoforms', action='store_true', help='Scrap all forms')
    parser.add_argument('--http-polution', action='store_true', help='HTTP polution')
    parser.add_argument('--xssget', action='store_true', help='XSS via GET')
    parser.add_argument('--xsspost', action='store_true', help='XSS via POST')
    parser.add_argument('--sqli', type=str, nargs='?', const="Normal",  help='SQLI via POST: currently supported: "Normal", "Insert", "Timing"')
    parser.add_argument('--postdata', nargs='*', help='Post Data')
    args = parser.parse_args()

    if args.http_polution:
        print(http_pollution(args.url, args.parameter))
    elif args.xssget:
        print(xss_get(args.url))
    elif args.xsspost:
        print(xss_post(args.url, args.autoforms, args.postdata))
    elif args.sqli:
        print(sqlinjection(args.url, args.sqli, args.autoforms, args.postdata))
    else:
        print("Nie podano odpowiedniego argumentu.")


if __name__ == "__main__":
    main()