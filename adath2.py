class HashTable:
    def __init__(self, size=10):
        self.size = size
        # Létrehozunk egy 'size' méretű listát, ahol minden elem egy üres lista (vödör)
        self.table = [[] for _ in range(self.size)]

    def _hash(self, key):
        """Beépített hash() függvény használata és az index kiszámítása a méret alapján."""
        return hash(key) % self.size

    def insert(self, key, value):
        """Beszúr vagy frissít egy kulcs-érték párt."""
        index = self._hash(key)
        bucket = self.table[index]

        # Ha a kulcs már létezik, frissítjük az értékét
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return

        # Ha még nem létezik, hozzáadjuk a vödör végéhez
        bucket.append((key, value))

    def get(self, key):
        """Visszaadja a kulcshoz tartozó értéket, vagy None-t ha nem találja."""
        index = self._hash(key)
        bucket = self.table[index]

        for k, v in bucket:
            if k == key:
                return v
        return None

    def remove(self, key):
        """Töröl egy kulcs-érték párt. Visszatér True-val ha sikeres, False-al ha nem volt ilyen kulcs."""
        index = self._hash(key)
        bucket = self.table[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                return True
        return False

    def display(self):
        """Kiírja a hash tábla tartalmát a terminálba."""
        for i, bucket in enumerate(self.table):
            print(f"Index {i:2}: {bucket}")


# --- TESZTELÉS ---
if __name__ == "__main__":
    ht = HashTable(size=5)

    print("1. Elemek beszúrása:")
    ht.insert("alma", 100)
    ht.insert("körte", 200)
    ht.insert("szilva", 300)
    ht.insert("barack", 400) # Ez lehet, hogy ütközik valamelyikkel
    ht.display()

    print("\n2. Keresés ('körte'):")
    print(f"A 'körte' értéke: {ht.get('körte')}")

    print("\n3. Törlés ('alma'):")
    ht.remove("alma")
    ht.display()