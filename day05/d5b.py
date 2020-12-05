from day05.d5a import read_seats, get_seat_ids

seats = read_seats('d5in.txt')
seat_ids = sorted(get_seat_ids(seats))

ix = 0
while seat_ids[ix + 1] == seat_ids[ix] + 1:
    ix += 1

print(seat_ids[ix] + 1)


