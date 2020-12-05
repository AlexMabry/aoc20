from util import decode_list


def read_seats(filename):
    lines = [n for n in open(filename).read().splitlines()]

    template = r'(?P<row>[FB]{7})(?P<col>[LR]{3})'
    return decode_list(lines, template)


def row_to_int(row):
    ret = 0
    if row[0] == 'B':
        ret += 64
    if row[1] == 'B':
        ret += 32
    if row[2] == 'B':
        ret += 16
    if row[3] == 'B':
        ret += 8
    if row[4] == 'B':
        ret += 4
    if row[5] == 'B':
        ret += 2
    if row[6] == 'B':
        ret += 1

    return ret


def col_to_int(row):
    ret = 0
    if row[0] == 'R':
        ret += 4
    if row[1] == 'R':
        ret += 2
    if row[2] == 'R':
        ret += 1

    return ret


def get_seat_ids(seat_list):
    return [row_to_int(seat.row) * 8 + col_to_int(seat.col) for seat in seat_list]


if __name__ == '__main__':
    seats = read_seats('d5in.txt')
    seat_ids = get_seat_ids(seats)

    print(max(seat_ids))
