from paloma_sdk.client.lcd import LCDClient, PaginationOptions

paloma = LCDClient(
    url="https://lcd.testnet.palomaswap.com/",
    chain_id="paloma-testnet-15",
)


pagopt = PaginationOptions(limit=3, count_total=True, reverse=True)


def test_signing_infos():
    result, _ = paloma.slashing.signing_infos()
    assert result is not None


def test_signing_infos_with_pagination():
    result, _ = paloma.slashing.signing_infos(pagopt)
    assert result is not None


# def test_signing_info():
#     result = paloma.slashing.signing_info(
#         "palomavalcons1qp67nk6gwqvnh95rwytpfwatcjtuxx4rxnlqvn"
#     )
#     assert result is not None


def test_parameters():
    result = paloma.slashing.parameters()
    assert result.get("signed_blocks_window")
    assert result.get("min_signed_per_window")
    assert result.get("downtime_jail_duration")
    assert result.get("slash_fraction_double_sign")
    assert result.get("slash_fraction_downtime")
