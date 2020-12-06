from util import decode_list


def read_seats(filename):
    lines = [n for n in open(filename).read().splitlines()]
    template = r'(?P<row>[FB]{7})(?P<col>[LR]{3})'
    return decode_list(lines, template)


def get_seat_id(seat):
    row = int(seat.row.replace('B', '1').replace('F', '0'), base=2)
    col = int(seat.col.replace('R', '1').replace('L', '0'), base=2)
    return row * 8 + col


def get_seat_ids(seats):
    return [get_seat_id(seat) for seat in seats]


if __name__ == '__main__':
    all_seats = read_seats('d5in.txt')
    seat_ids = get_seat_ids(all_seats)

    largest_seat_id = max(seat_ids)
    print(largest_seat_id)
