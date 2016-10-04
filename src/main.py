from swedishtrainer import Swedishtrainer

main = Swedishtrainer()

main.read_dictionary_file(main.select_dictionary_prompt())
main.generate_questions()