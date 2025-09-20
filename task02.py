class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def insert(root, key):
    """Вставляє новий ключ у BST і повертає корінь (можливо оновлений)."""
    if root is None:
        return Node(key)

    if key < root.val:
        root.left = insert(root.left, key)   # йдемо вліво, якщо ключ менший
    else:
        root.right = insert(root.right, key) # йдемо вправо, якщо ключ більший або рівний

    return root


def postorder_traversal(root):
    """Повертає суму всіх значень у дереві за допомогою postorder обходу."""
    if root is None:
        return 0
    return postorder_traversal(root.left) + postorder_traversal(root.right) + root.val


if __name__ == "__main__":
    # Створюємо дерево за допомогою insert
    root = None
    # keys = [5, 3, 7, 2, 4, 6, 8]  # значення, які додаємо у BST
    keys = [7, 21, 3, 18, 45, 32, 778]  # значення, які додаємо у BST

    for key in keys:
        root = insert(root, key)

    # Обчислюємо суму та виводимо лише її
    total_sum = postorder_traversal(root)
    print(total_sum)