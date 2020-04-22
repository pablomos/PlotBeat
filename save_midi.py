def times_to_quarters(times, bpm):
    return [t * bpm / 60. for t in times]

def test_times_to_quarters():
    times = [1]
    bpm = 60
    quarters = times_to_quarters(times, bpm)
    if quarters != [1]:
        raise Exception('Second not converted correctly to quarters')
    faster_bpm = 90
    faster_quarters = times_to_quarters(times, faster_bpm)
    if faster_quarters[0] <= quarters[0]:
        raise Exception('Faster beat rate does not mean more quarters')

test_times_to_quarters()
