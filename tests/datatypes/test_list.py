from .. utils import TranspileTestCase, UnaryOperationTestCase, BinaryOperationTestCase, InplaceOperationTestCase


class ListTests(TranspileTestCase):
    def test_creation(self):
        self.assertCodeExecution("""
            x = [1, 2, 3, 4, 5]
            print(x)
            """)

    def test_getitem(self):
        # Simple positive index
        self.assertCodeExecution("""
            x = [1, 2, 3, 4, 5]
            print(x[2])
            """)

        # Simple negative index
        self.assertCodeExecution("""
            x = [1, 2, 3, 4, 5]
            print(x[-2])
            """)

        # Positive index out of range
        self.assertCodeExecution("""
            x = [1, 2, 3, 4, 5]
            print(x[10])
            """)

        # Negative index out of range
        self.assertCodeExecution("""
            x = [1, 2, 3, 4, 5]
            print(x[-10])
            """)

    # def test_list_comprehensions(self):
    #     self.assertCodeExecution("""
    #         x = [1, 2, 3]
    #         y = [v**2 for v in x]
    #         print(y)
    #         """)


class UnaryListOperationTests(UnaryOperationTestCase, TranspileTestCase):
    values = ['[]', '[1, 2, 3, 4, 5]']

    not_implemented = [
        'test_unary_positive',
        'test_unary_negative',
        'test_unary_not',
        'test_unary_invert',
    ]


class BinaryListOperationTests(BinaryOperationTestCase, TranspileTestCase):
    values = ['[]', '[1, 2, 3, 4, 5]']

    not_implemented = [
        'test_add_bool',
        'test_multiply_bool',
        'test_subscr_bool',

        'test_add_bytearray',
        'test_subtract_bytearray',
        'test_multiply_bytearray',
        'test_floor_divide_bytearray',
        'test_true_divide_bytearray',
        'test_modulo_bytearray',
        'test_power_bytearray',
        'test_subscr_bytearray',
        'test_lshift_bytearray',
        'test_rshift_bytearray',
        'test_and_bytearray',
        'test_xor_bytearray',
        'test_or_bytearray',

        'test_add_bytes',
        'test_subtract_bytes',
        'test_multiply_bytes',
        'test_floor_divide_bytes',
        'test_true_divide_bytes',
        'test_modulo_bytes',
        'test_power_bytes',
        'test_subscr_bytes',
        'test_lshift_bytes',
        'test_rshift_bytes',
        'test_and_bytes',
        'test_xor_bytes',
        'test_or_bytes',

        'test_add_class',
        'test_subtract_class',
        'test_multiply_class',
        'test_floor_divide_class',
        'test_true_divide_class',
        'test_modulo_class',
        'test_power_class',
        'test_subscr_class',
        'test_lshift_class',
        'test_rshift_class',
        'test_and_class',
        'test_xor_class',
        'test_or_class',

        'test_add_complex',
        'test_subtract_complex',
        'test_multiply_complex',
        'test_floor_divide_complex',
        'test_true_divide_complex',
        'test_modulo_complex',
        'test_power_complex',
        'test_subscr_complex',
        'test_lshift_complex',
        'test_rshift_complex',
        'test_and_complex',
        'test_xor_complex',
        'test_or_complex',

        'test_add_dict',
        'test_subtract_dict',
        'test_multiply_dict',
        'test_floor_divide_dict',
        'test_true_divide_dict',
        'test_modulo_dict',
        'test_power_dict',
        'test_subscr_dict',
        'test_lshift_dict',
        'test_rshift_dict',
        'test_and_dict',
        'test_xor_dict',
        'test_or_dict',

        'test_add_float',
        'test_multiply_float',
        'test_subscr_float',

        'test_add_frozenset',
        'test_subtract_frozenset',
        'test_multiply_frozenset',
        'test_floor_divide_frozenset',
        'test_true_divide_frozenset',
        'test_modulo_frozenset',
        'test_power_frozenset',
        'test_subscr_frozenset',
        'test_lshift_frozenset',
        'test_rshift_frozenset',
        'test_and_frozenset',
        'test_xor_frozenset',
        'test_or_frozenset',

        'test_add_int',
        'test_multiply_int',

        'test_add_list',
        'test_multiply_list',
        'test_subscr_list',

        'test_add_set',
        'test_multiply_set',
        'test_subscr_set',

        'test_add_str',
        'test_multiply_str',

        'test_add_tuple',
        'test_multiply_tuple',
        'test_subscr_tuple',
    ]


class InplaceListOperationTests(InplaceOperationTestCase, TranspileTestCase):
    values = ['[]', '[1, 2, 3, 4, 5]']

    not_implemented = [
        'test_add_bool',
        'test_subtract_bool',
        'test_multiply_bool',
        'test_floor_divide_bool',
        'test_true_divide_bool',
        'test_modulo_bool',
        'test_power_bool',
        'test_lshift_bool',
        'test_rshift_bool',
        'test_and_bool',
        'test_xor_bool',
        'test_or_bool',

        'test_add_bytearray',
        'test_subtract_bytearray',
        'test_multiply_bytearray',
        'test_floor_divide_bytearray',
        'test_true_divide_bytearray',
        'test_modulo_bytearray',
        'test_power_bytearray',
        'test_lshift_bytearray',
        'test_rshift_bytearray',
        'test_and_bytearray',
        'test_xor_bytearray',
        'test_or_bytearray',

        'test_add_bytes',
        'test_subtract_bytes',
        'test_multiply_bytes',
        'test_floor_divide_bytes',
        'test_true_divide_bytes',
        'test_modulo_bytes',
        'test_power_bytes',
        'test_lshift_bytes',
        'test_rshift_bytes',
        'test_and_bytes',
        'test_xor_bytes',
        'test_or_bytes',

        'test_add_class',
        'test_subtract_class',
        'test_multiply_class',
        'test_floor_divide_class',
        'test_true_divide_class',
        'test_modulo_class',
        'test_power_class',
        'test_lshift_class',
        'test_rshift_class',
        'test_and_class',
        'test_xor_class',
        'test_or_class',

        'test_add_complex',
        'test_subtract_complex',
        'test_multiply_complex',
        'test_floor_divide_complex',
        'test_true_divide_complex',
        'test_modulo_complex',
        'test_power_complex',
        'test_lshift_complex',
        'test_rshift_complex',
        'test_and_complex',
        'test_xor_complex',
        'test_or_complex',

        'test_add_dict',
        'test_subtract_dict',
        'test_multiply_dict',
        'test_floor_divide_dict',
        'test_true_divide_dict',
        'test_modulo_dict',
        'test_power_dict',
        'test_lshift_dict',
        'test_rshift_dict',
        'test_and_dict',
        'test_xor_dict',
        'test_or_dict',

        'test_add_float',
        'test_subtract_float',
        'test_multiply_float',
        'test_floor_divide_float',
        'test_true_divide_float',
        'test_modulo_float',
        'test_power_float',
        'test_lshift_float',
        'test_rshift_float',
        'test_and_float',
        'test_xor_float',
        'test_or_float',

        'test_add_frozenset',
        'test_subtract_frozenset',
        'test_multiply_frozenset',
        'test_floor_divide_frozenset',
        'test_true_divide_frozenset',
        'test_modulo_frozenset',
        'test_power_frozenset',
        'test_lshift_frozenset',
        'test_rshift_frozenset',
        'test_and_frozenset',
        'test_xor_frozenset',
        'test_or_frozenset',

        'test_add_int',
        'test_subtract_int',
        'test_multiply_int',
        'test_floor_divide_int',
        'test_true_divide_int',
        'test_modulo_int',
        'test_power_int',
        'test_lshift_int',
        'test_rshift_int',
        'test_and_int',
        'test_xor_int',
        'test_or_int',

        'test_add_list',
        'test_subtract_list',
        'test_multiply_list',
        'test_floor_divide_list',
        'test_true_divide_list',
        'test_modulo_list',
        'test_power_list',
        'test_lshift_list',
        'test_rshift_list',
        'test_and_list',
        'test_xor_list',
        'test_or_list',

        'test_add_set',
        'test_subtract_set',
        'test_multiply_set',
        'test_floor_divide_set',
        'test_true_divide_set',
        'test_modulo_set',
        'test_power_set',
        'test_lshift_set',
        'test_rshift_set',
        'test_and_set',
        'test_xor_set',
        'test_or_set',

        'test_add_str',
        'test_subtract_str',
        'test_multiply_str',
        'test_floor_divide_str',
        'test_true_divide_str',
        'test_modulo_str',
        'test_power_str',
        'test_lshift_str',
        'test_rshift_str',
        'test_and_str',
        'test_xor_str',
        'test_or_str',

        'test_add_tuple',
        'test_subtract_tuple',
        'test_multiply_tuple',
        'test_floor_divide_tuple',
        'test_true_divide_tuple',
        'test_modulo_tuple',
        'test_power_tuple',
        'test_lshift_tuple',
        'test_rshift_tuple',
        'test_and_tuple',
        'test_xor_tuple',
        'test_or_tuple',
    ]
