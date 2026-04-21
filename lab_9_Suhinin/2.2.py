def format_address(city,street,house,apartment = None):
    if apartment == None:
        print(f"м.{city}, вул.{street}, буд.{house}")
    else:
        print(f"м.{city}, вул.{street}, буд.{house}, кв.{apartment}")
format_address("Київ", "Хрещатик", "1", "42")