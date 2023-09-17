def get_animals_details(animal):
    if not animal:
        return 'No animal'

    animal_type = animal.get('type')
    animal_name = animal.get('name')
    animal_gender = animal.get('gender')

    if not animal_type:
        return 'No animal type'
    
    if not animal_name:
        return 'No animal name'
    
    if not animal_gender:
        return 'No animal gender'

    return f"{animal_name} is a {animal_gender} {animal_type}"
