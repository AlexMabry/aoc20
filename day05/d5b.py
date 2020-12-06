from day05.d5a import read_seats, get_seat_ids


def find_my_seat(sids):
    sorted_ids = sorted(sids)
    for ix, sid in enumerate(sorted_ids):
        if sorted_ids[ix + 1] != sid + 1:
            return sid + 1


if __name__ == '__main__':
    all_seats = read_seats('d5in.txt')
    seat_ids = get_seat_ids(all_seats)

    my_seat = find_my_seat(seat_ids)
    print(my_seat)


