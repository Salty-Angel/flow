from state.models import Node


def print_project(project):
    project.head.display()


def do_task(task_id, user):
    task = Node.objects.get(pk=task_id)
    task.complete(user)


def finish_phase(phase_id, user):
    phase = Node.objects.get(pk=phase_id)
    phase.complete(user)