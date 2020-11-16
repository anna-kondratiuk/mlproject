if __name__ == '__main__':
    description = 'stkrgcp_description'
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('--coords',
                        nargs='+',
                        help='mails to send hardware alerts',
                        required=False)
    parser.add_argument('--prod',
                        action='store_true',
                        default=False,
                        help='Example here')
    args = parser.parse_args()
    lon1, lat1, lon2, lat2 = args.coords
    dist = haversine(float(lon1), float(lat1), float(lon2), float(lat2))
    print(colored("###### Distance ######", "blue"))
    print(colored(dist, "red"))
