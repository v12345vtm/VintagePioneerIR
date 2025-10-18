'''
author : v12345vtmm
How it works:
The script reads inputs from the user.
Converts Pronto HEX IR code to raw pulse durations.
Generates the YAML button snippet.
Opens (or creates if missing) the file buttons.yaml in append mode and writes the YAML.
Prints a confirmation message.
This way, you can keep adding new buttons to your YAML file on each run without overwriting previous content. Just run the script and provide inputs as needed for various remote commands.
'''




def pronto_to_raw(pronto):
    codes = [int(x, 16) for x in pronto.split()]
    freq = 1000000 / (codes[1] * 0.241246) if codes[1] != 0 else 38000
    unit = 1000000 / freq
    length = codes[3] * 2
    burst_pairs = codes[4:4 + length]
    raw = []
    for i, val in enumerate(burst_pairs):
        t = int(val * unit)
        raw.append(t if i % 2 == 0 else -t)
    return freq, raw


def generate_button_yaml(name, repeat, pronto):
    freq, raw = pronto_to_raw(pronto)
    raw_str = ", ".join(str(x) for x in raw)
    yaml = f'''#button:
  - platform: template
    name: "{name}"    
    on_press:
      - remote_transmitter.transmit_raw:
          repeat: {repeat}
          carrier_frequency: {int(freq)}Hz
          code: [{raw_str}]

'''
    return yaml


if __name__ == "__main__":
    name = input("Enter button name: ")
    repeat = int(input("Enter repeat count (integer): eg:2  : "))
    pronto = input("Enter Pronto HEX code string: eg : 0000 0067 0000 0022 0155 ....  : ")
    yaml_output = generate_button_yaml(name, repeat, pronto)

    with open("buttons.yaml", "a") as file:
        file.write(yaml_output)

    print(f"YAML button for '{name}' appended to buttons.yaml")
