import pickle

person = {
    "name": "sajjad",
    "age": 16
}

pickle_result = pickle.dumps(person)

print(pickle_result)
print(pickle.loads(pickle_result))

with open('mp_06_pickle.pickle', 'wb') as f:
    pickle.dump(person, f)
with open('mp_06_pickle.pickle', 'rb') as f:
    result = pickle.load(f)
    print(result)
