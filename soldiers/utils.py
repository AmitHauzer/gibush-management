

def tasks_by_percent(after, before):
    soldiers_before = before.count()
    soldiers_after = after.count()
    all = soldiers_after + soldiers_before
    percent = round((((all - soldiers_before)/all) * 100), 2)
    return percent
