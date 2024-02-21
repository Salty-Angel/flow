from state.models import Node
from state.models.node import NodeType


def print_project(project):
    project.head.refresh_from_db()
    print('\n\n')
    project.head.display()
    print('\n\n')


def do_task(task_id, user):
    task = Node.objects.get(pk=task_id)
    task.complete(user)


def finish_phase(phase_id, user):
    phase = Node.objects.get(pk=phase_id)
    phase.complete(user)


def status(project):
    def title(t):
        return f'\n-- {t} --'

    def info(i):
        return f'   {i}'

    print(title('Current Phase'))
    for phase in Node.objects.filter(project=project, completed=False, follows__completed=True):
        print(info(f'[{phase.id}] {phase.title}'))

    print(title('Log'))
    all_phases = Node.objects.filter(project=project, node_type=NodeType.PHASE)
    completed_phases = Node.objects.filter(project=project, completed=True, node_type=NodeType.PHASE)
    print(info(f'[{completed_phases.count()}/{all_phases.count()}] completed.'))
    print('\n')
    for phase in completed_phases.order_by('completed_on'):
        print(
            info(
                f'[{phase.id:2}] {phase.title:20} completed by {phase.completed_by.name:11} on {phase.completed_on}.'  # noqa:
            )
        )
    print('\n')


def reset(project):
    do_you_wanna = input('Are you sure you want to reset? (y/n) ')
    if do_you_wanna.lower() == 'y':
        Node.objects.filter(project=project).update(completed=False, completed_on=None)
