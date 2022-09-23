from paloma_sdk.core.bank import MsgMultiSend, MsgSend


def test_deserializes_msg_send(load_msg_examples):
    data = {
        "@type": "/cosmos.bank.v1beta1.MsgSend",
        "from_address": "paloma1y4umfuqfg76t8mfcff6zzx7elvy93jtp4xcdvw",
        "to_address": "paloma1v9ku44wycfnsucez6fp085f5fsksp47u9x8jr4",
        "amount": [{"denom": "uluna", "amount": "8102024952"}],
    }

    assert MsgSend.from_data(data).to_data() == data


def test_deserializes_msg_multi_send(load_msg_examples):
    data = {
        "@type": "/cosmos.bank.v1beta1.MsgMultiSend",
        "inputs": [
            {
                "address": "paloma1fex9f78reuwhfsnc8sun6mz8rl9zwqh03fhwf3",
                "coins": [{"denom": "ukrw", "amount": "1"}],
            },
            {
                "address": "paloma1gg64sjt947atmh45ls45avdwd89ey4c4r72u9h",
                "coins": [{"denom": "ukrw", "amount": "6900000000"}],
            },
            {
                "address": "paloma1yh9u2x8phrh2dan56nntgpmg7xnjrwtldhgmyu",
                "coins": [{"denom": "ukrw", "amount": "1000000"}],
            },
            {
                "address": "paloma1c5a0njk9q6q6nheja8gp4ymt2c0qspd8ggpg49",
                "coins": [{"denom": "ukrw", "amount": "16430000000"}],
            },
            {
                "address": "paloma1psswnm8mvy9qg5z4cxc2nvptc9dx62r4tvfrmh",
                "coins": [{"denom": "ukrw", "amount": "9900000000"}],
            },
            {
                "address": "paloma10lgpfm8wjrl4d9datzw6r6dl83k977afzel4t5",
                "coins": [{"denom": "ukrw", "amount": "15800000000"}],
            },
            {
                "address": "paloma13uj5qs3lcqtffqtu6aa089uf6a2pusgwndzzch",
                "coins": [{"denom": "ukrw", "amount": "6900000000"}],
            },
        ],
        "outputs": [
            {
                "address": "paloma1fex9f78reuwhfsnc8sun6mz8rl9zwqh03fhwf3",
                "coins": [{"denom": "ukrw", "amount": "1"}],
            },
            {
                "address": "paloma105rz2q5a4w7nv7239tl9c4px5cjy7axx3axf6p",
                "coins": [{"denom": "ukrw", "amount": "6900000000"}],
            },
            {
                "address": "paloma1fex9f78reuwhfsnc8sun6mz8rl9zwqh03fhwf3",
                "coins": [{"denom": "ukrw", "amount": "1000000"}],
            },
            {
                "address": "paloma105rz2q5a4w7nv7239tl9c4px5cjy7axx3axf6p",
                "coins": [{"denom": "ukrw", "amount": "16430000000"}],
            },
            {
                "address": "paloma105rz2q5a4w7nv7239tl9c4px5cjy7axx3axf6p",
                "coins": [{"denom": "ukrw", "amount": "9900000000"}],
            },
            {
                "address": "paloma105rz2q5a4w7nv7239tl9c4px5cjy7axx3axf6p",
                "coins": [{"denom": "ukrw", "amount": "15800000000"}],
            },
            {
                "address": "paloma105rz2q5a4w7nv7239tl9c4px5cjy7axx3axf6p",
                "coins": [{"denom": "ukrw", "amount": "6900000000"}],
            },
        ],
    }

    assert MsgMultiSend.from_data(data).to_data() == data
