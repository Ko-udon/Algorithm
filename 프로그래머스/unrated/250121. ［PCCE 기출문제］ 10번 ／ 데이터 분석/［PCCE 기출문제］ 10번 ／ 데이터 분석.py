def solution(data, ext, val_ext, sort_by):
    answer = []
    category = [ "code", "date", "maximum", "remain" ]

    for d in data:
        if d[category.index(ext)] < val_ext:
            answer.append(d)

    return sorted(answer, key=lambda x: x[category.index(sort_by)])