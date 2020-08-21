

let change_url = "{% url 'userSystem:documentMangement'  %}" + "/" + "{{ username }}" + "{{ password }}"
window.open(change_url)

