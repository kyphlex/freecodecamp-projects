def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    first_line = ""
    second_line = ""
    dashes_line = ""
    answers_line = ""

    for i, problem in enumerate(problems):
        parts = problem.split()

        if len(parts) != 3:
            return "Error: Each problem must contain two operands and an operator."

        left, operator, right = parts

        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."

        if not left.isdigit() or not right.isdigit():
            return "Error: Numbers must only contain digits."

        if len(left) > 4 or len(right) > 4:
            return "Error: Numbers cannot be more than four digits."

        width = max(len(left), len(right)) + 2

        top = left.rjust(width)
        bottom = operator + right.rjust(width - 1)
        dashes = '-' * width
        answer = ""

        if show_answers:
            result = str(eval(problem))
            answer = result.rjust(width)

        spacer = "    " if i < len(problems) - 1 else ""

        first_line += top + spacer
        second_line += bottom + spacer
        dashes_line += dashes + spacer
        if show_answers:
            answers_line += answer + spacer

    if show_answers:
        return f"{first_line}\n{second_line}\n{dashes_line}\n{answers_line}"
    else:
        return f"{first_line}\n{second_line}\n{dashes_line}"
