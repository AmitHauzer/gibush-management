from soldiers.models import Soldier


def shalishut_tasks_by_percent():
    soldiers_before = Soldier.objects.filter(
        soldier_status=Soldier.SoldierStatus.WAITING_FOR_CLINIC)
    soldiers_after = Soldier.objects.exclude(Q(soldier_status=Soldier.SoldierStatus.WAITING_FOR_CLINIC) | Q(
        soldier_status=Soldier.SoldierStatus.WAITING_FOR_SHALISHUT))
    all = soldiers_after + soldiers_before
    percent = round((((all - soldiers_before)/all) * 100), 2)
    return percent
