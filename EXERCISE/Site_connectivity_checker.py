import urllib.request as urllib


def main(url):
    print("Checking connectivity")
    response = urllib.urlopen(url)
    print(f"Connected to {url} successfully.")
    print(f"The response code is {response.getcode()}")

print("This is a site connectivity checker program ")
input_url = input("Type in your url: ")

main(input_url)