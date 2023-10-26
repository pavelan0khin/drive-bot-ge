import sys

boolean_choices = ((True, "Yes"), (False, "No"))


def progress_bar(
    current, total, bar_length=50, char="█", fill_char="-", color="\033[92m", endcolor="\033[0m"
):
    progress = float(current) / total
    arrow = char * int(round(progress * bar_length) - 1)
    spaces = fill_char * (bar_length - len(arrow))
    sys.stdout.write(f"\r[{color}{arrow}{spaces}{endcolor}] {current}/{total}")
    sys.stdout.flush()
