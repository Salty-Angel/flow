from state.actions import (  # noqa: F401,
    do_task,
    finish_phase,
    print_project,
    reset,
    status,
)
from state.models import Project, User, Node  # noqa: F401

gandolf = User.objects.get(name='Gandolf')
gary = User.objects.get(name='Gary Gygax')
goldmoon = User.objects.get(name='Goldmoon')
raistlin = User.objects.get(name='Raistlin')
proj = Project.objects.first()

print_project(proj)
