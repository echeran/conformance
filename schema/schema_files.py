# Points to file names for each supported JSON files.

ALL_TEST_TYPES = ['collation_short',
                  'datetime_fmt',
                  'lang_names',
                  'likely_subtags',
                  'lang_names',
                  'list_fmt',
                  'message_fmt2',
                  'number_format',
                  'plural_rules',
                  'rdt_fmt'
                  ]

TEST_FILE_TO_TEST_TYPE_MAP = {
    'collation_test': 'collation_short',
    'datetime_fmt_test_file': 'datetime_fmt',
    'lang_names_test_file': 'lang_names',
    'likely_subtags_test': 'likely_subtags',
    'list_fmt_test_file': 'list_fmt',
    'message_fmt2_test_file': 'message_fmt2',
    'num_fmt_test_file': 'number_fmt',
    'plural_rules_test_file': 'plural_rules',
    'rdt_fmt_test_file': 'rdt'
}

SCHEMA_FILE_MAP = {
    "collation_short": {
        "test_data": {
            "schema_file": "collation_short/test_schema.json",
            "prod_file": "collation_test.json"
        },
        "verify_data": {
            # For, eventually, checking the expected output created by the test generator.

            "schema_file": "collation_short/verify_schema.json",
            "prod_file": "pass.json"
        },
        "result_data": {
            # For checking test outputs.
            "schema_file": "collation_short/result_schema.json",
            "prod_file": "collation_test.json"
        }
    },

    "datetime_fmt": {
        "test_data": {
            "schema_file": "datetime_fmt/test_schema.json",
            'prod_file': 'datetime_test_file.json'
        },
        "verify_data": {
            "schema_file": "datetime_fmt/verify_schema.json",
            'prod_file': 'pass.json'
        },
        "result_data": {
            "schema_file": "datetime_fmt/result_schema.json",
            "prod_file": 'datetime_test_file.json'
        }
    },

    "number_format": {
        "test_data": {
            "schema_file": "number_format/test_schema.json",
            'prod_file': 'num_fmt_test_file.json'
        },
        "verify_data": {
            "schema_file": "number_format/verify_schema.json",
            'prod_file': 'pass.json'
        },
        "result_data": {
            "schema_file": "number_format/result_schema.json",
            "prod_file": 'num_fmt_test_file.json'
        }
    },

    "number_fmt": {
        "test_data": {
            "schema_file": "number_format/test_schema.json",
            'prod_file': 'num_fmt_test_file.json'
        },
        "verify_data": {
            "schema_file": "number_format/verify_schema.json",
            'prod_file': 'pass.json'
        },
        "result_data": {
            "schema_file": "number_format/result_schema.json",
            "prod_file": 'num_fmt_test_file.json'
        }
    },

    "lang_names": {
        "test_data": {
            "schema_file": "lang_names/test_schema.json",
            'prod_file': 'lang_name_test_file.json'
        },
        "verify_data": {
            "schema_file": "lang_names/verify_schema.json",
            'prod_file': 'pass.json'
        },
        "result_data": {
            "schema_file": "lang_names/result_schema.json",
            "prod_file": "lang_name_test_file.json"
        }
    },
    "likely_subtags": {
        "test_data": {
            "schema_file": "likely_subtags/test_schema.json",
            'prod_file': 'likely_subtags_test.json'
        },
        "verify_data": {
            "schema_file": "likely_subtags/verify_schema.json",
            'prod_file': 'likely_subtags_verify.json'
        },
        "result_data": {
            "schema_file": "likely_subtags/result_schema.json",
            "prod_file": "likely_subtags_test.json"
        }
    },
    "list_fmt": {
        "test_data": {
            "schema_file": "list_fmt/test_schema.json",
            'prod_file': 'list_fmt.json'
        },
        "verify_data": {
            "schema_file": "list_fmt/verify_schema.json",
            'prod_file': 'list_fmt.json'
        },
        "result_data": {
            "schema_file": "list_fmt/result_schema.json",
            "prod_file": "list_fmt_test.json"
        }
    },
    "plural_rules" : {
        "test_data": {
            "schema_file": "plural_rules/test_schema.json",
            'prod_file': 'plural_rules.json'
        },
        "verify_data": {
            "schema_file": "plural_rules/verify_schema.json",
            'prod_file': 'plural_rules.json'
        },
        "result_data": {
            "schema_file": "plural_rules/result_schema.json",
            "prod_file": "plural_rules.json"
        }
    },
    "message_fmt2": {
        "test_data": {
            "schema_file": "message_fmt2/test_schema.json",
            'prod_file': 'message_fmt2_test.json'
        },
        "verify_data": {
            "schema_file": "message_fmt2/verify_schema.json",
            'prod_file': 'message_fmt2_verify.json'
        },
        "result_data": {
            "schema_file": "message_fmt2/result_schema.json",
            'prod_file': 'message_fmt2_result.json'
        }
    },
    "rdt_fmt": {
        "test_data": {
            "schema_file": "rdt_fmt/test_schema.json",
            'prod_file': 'rdt_fmt.json'
        },
        "verify_data": {
            "schema_file": "rdt_fmt/verify_schema.json",
            'prod_file': 'rdt_fmt.json'
        },
        "result_data": {
            "schema_file": "plural_rules/result_schema.json",
            "prod_file": "rdt_fmt.json"
        }
    },
    # Additional tests

}
