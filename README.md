# Алгоритми пошуку (ДЗ)

### Завдання 1

Додати метод `delete` для видалення пар ключ-значення таблиці `HashTable`, яка реалізована в конспекті.

### Завдання 2

Реалізувати двійковий пошук для відсортованого масиву з дробовими числами. Написана функція для двійкового пошуку повинна повертати кортеж, де першим елементом є кількість ітерацій, потрібних для знаходження елемента. Другим елементом має бути "верхня межа" — це найменший елемент, який є більшим або рівним заданому значенню.

### Завдання 3

Порівняти ефективність алгоритмів пошуку підрядка: Боєра-Мура, Кнута-Морріса-Пратта та Рабіна-Карпа на основі двох текстових файлів (стаття 1, стаття 2). Використовуючи `timeit`, треба виміряти час виконання кожного алгоритму для двох видів підрядків: одного, що дійсно існує в тексті, та іншого — вигаданого (вибір підрядків за вашим бажанням). На основі отриманих даних визначити найшвидший алгоритм для кожного тексту окремо та в цілому.

## Висновки завдання № 3

У першій статті найшвидшим для пошуку реального підрядка виявився алгоритм Боєра-Мура, тоді як для вигаданого — Кнута-Морріса-Пратта. У другій статті алгоритм Боєра-Мура знову продемонстрував найкращу швидкість для реального підрядка, а Кнута-Морріса-Пратта — для вигаданого.  

Загалом, алгоритм Боєра-Мура показав найвищу ефективність для обох текстів. Це, ймовірно, зумовлено специфікою самих текстів і вибраних фрагментів.
