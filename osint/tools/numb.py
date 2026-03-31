import phonenumbers
from phonenumbers import PhoneNumberFormat, PhoneNumberType, NumberParseException, Leniency

def parse(number: str, region: str = None) -> phonenumbers.PhoneNumber: return phonenumbers.parse(number, region)
def format_e164(phone: phonenumbers.PhoneNumber) -> str: return phonenumbers.format_number(phone, PhoneNumberFormat.E164)
def format_international(phone: phonenumbers.PhoneNumber) -> str: return phonenumbers.format_number(phone, PhoneNumberFormat.INTERNATIONAL)
def format_national(phone: phonenumbers.PhoneNumber) -> str: return phonenumbers.format_number(phone, PhoneNumberFormat.NATIONAL)
def format_rfc3966(phone: phonenumbers.PhoneNumber) -> str: return phonenumbers.format_number(phone, PhoneNumberFormat.RFC3966)
def format_original(phone: phonenumbers.PhoneNumber, region: str) -> str: return phonenumbers.format_in_original_format(phone, region)
def format_for_mobile(phone: phonenumbers.PhoneNumber, region_calling_from: str, with_formatting: bool = True) -> str: return phonenumbers.format_number_for_mobile_dialing(phone, region_calling_from, with_formatting)
def format_out_of_country(phone: phonenumbers.PhoneNumber, region_calling_from: str) -> str: return phonenumbers.format_out_of_country_calling_number(phone, region_calling_from)
def format_out_of_country_alpha(phone: phonenumbers.PhoneNumber, region_calling_from: str) -> str: return phonenumbers.format_out_of_country_keeping_alpha_chars(phone, region_calling_from)
def format_with_carrier(phone: phonenumbers.PhoneNumber, carrier_code: str) -> str: return phonenumbers.format_national_number_with_carrier_code(phone, carrier_code)
def format_with_preferred_carrier(phone: phonenumbers.PhoneNumber, fallback_carrier_code: str) -> str: return phonenumbers.format_national_number_with_preferred_carrier_code(phone, fallback_carrier_code)
def format_by_pattern(phone: phonenumbers.PhoneNumber, number_format: int, user_defined_formats: list) -> str: return phonenumbers.format_by_pattern(phone, number_format, user_defined_formats)
def is_valid(phone: phonenumbers.PhoneNumber) -> bool: return phonenumbers.is_valid_number(phone)
def is_valid_for_region(phone: phonenumbers.PhoneNumber, region: str) -> bool: return phonenumbers.is_valid_number_for_region(phone, region)
def is_possible(phone: phonenumbers.PhoneNumber) -> bool: return phonenumbers.is_possible_number(phone)
def is_possible_string(number: str, region: str) -> bool: return phonenumbers.is_possible_number_string(number, region)
def is_possible_with_reason(phone: phonenumbers.PhoneNumber) -> int: return phonenumbers.is_possible_number_with_reason(phone)
def is_possible_for_type(phone: phonenumbers.PhoneNumber, num_type: int) -> bool: return phonenumbers.is_possible_number_for_type(phone, num_type)
def is_possible_for_type_with_reason(phone: phonenumbers.PhoneNumber, num_type: int) -> int: return phonenumbers.is_possible_number_for_type_with_reason(phone, num_type)
def is_alpha(number: str) -> bool: return phonenumbers.is_alpha_number(number)
def is_nanpa(region: str) -> bool: return phonenumbers.is_nanpa_country(region)
def is_geographical(phone: phonenumbers.PhoneNumber) -> bool: return phonenumbers.is_number_geographical(phone)
def is_geographical_type(num_type: int, country_code: int) -> bool: return phonenumbers.is_number_type_geographical(num_type, country_code)
def is_internationally_dialable(phone: phonenumbers.PhoneNumber) -> bool: return phonenumbers.can_be_internationally_dialled(phone)
def is_portable_region(region: str) -> bool: return phonenumbers.is_mobile_number_portable_region(region)
def get_number_type(phone: phonenumbers.PhoneNumber) -> int: return phonenumbers.number_type(phone)
def get_region(phone: phonenumbers.PhoneNumber) -> str: return phonenumbers.region_code_for_number(phone)
def get_region_for_code(country_code: int) -> str: return phonenumbers.region_code_for_country_code(country_code)
def get_regions_for_code(country_code: int) -> list: return list(phonenumbers.region_codes_for_country_code(country_code))
def get_country_code(region: str) -> int: return phonenumbers.country_code_for_region(region)
def get_country_code_valid(region: str) -> int: return phonenumbers.country_code_for_valid_region(region)
def get_mobile_token(country_code: int) -> str: return phonenumbers.country_mobile_token(country_code)
def get_national_number(phone: phonenumbers.PhoneNumber) -> str: return phonenumbers.national_significant_number(phone)
def get_area_code_length(phone: phonenumbers.PhoneNumber) -> int: return phonenumbers.length_of_geographical_area_code(phone)
def get_ndc_length(phone: phonenumbers.PhoneNumber) -> int: return phonenumbers.length_of_national_destination_code(phone)
def get_ndd_prefix(region: str, strip_non_digits: bool = False) -> str: return phonenumbers.ndd_prefix_for_region(region, strip_non_digits)
def get_example_number(region: str) -> phonenumbers.PhoneNumber: return phonenumbers.example_number(region)
def get_example_number_for_type(region: str, num_type: int) -> phonenumbers.PhoneNumber: return phonenumbers.example_number_for_type(region, num_type)
def get_example_number_non_geo(country_code: int) -> phonenumbers.PhoneNumber: return phonenumbers.example_number_for_non_geo_entity(country_code)
def get_invalid_example_number(region: str) -> phonenumbers.PhoneNumber: return phonenumbers.invalid_example_number(region)
def get_supported_regions() -> set: return phonenumbers.SUPPORTED_REGIONS
def get_supported_calling_codes() -> set: return set(phonenumbers.supported_calling_codes())
def get_supported_types_for_region(region: str) -> set: return phonenumbers.supported_types_for_region(region)
def get_supported_types_non_geo(country_code: int) -> set: return phonenumbers.supported_types_for_non_geo_entity(country_code)
def get_country_code_to_regions() -> dict: return {k: list(v) for k, v in phonenumbers.COUNTRY_CODE_TO_REGION_CODE.items()}
def is_possible_short(phone: phonenumbers.PhoneNumber) -> bool: return phonenumbers.is_possible_short_number(phone)
def is_possible_short_for_region(phone: phonenumbers.PhoneNumber, region: str) -> bool: return phonenumbers.is_possible_short_number_for_region(phone, region)
def is_valid_short(phone: phonenumbers.PhoneNumber) -> bool: return phonenumbers.is_valid_short_number(phone)
def is_valid_short_for_region(phone: phonenumbers.PhoneNumber, region: str) -> bool: return phonenumbers.is_valid_short_number_for_region(phone, region)
def get_short_cost(phone: phonenumbers.PhoneNumber) -> int: return phonenumbers.expected_cost(phone)
def get_short_cost_for_region(phone: phonenumbers.PhoneNumber, region: str) -> int: return phonenumbers.expected_cost_for_region(phone, region)
def is_emergency(number: str, region: str) -> bool: return phonenumbers.is_emergency_number(number, region)
def connects_to_emergency(number: str, region: str) -> bool: return phonenumbers.connects_to_emergency_number(number, region)
def is_carrier_specific(phone: phonenumbers.PhoneNumber) -> bool: return phonenumbers.is_carrier_specific(phone)
def is_carrier_specific_for_region(phone: phonenumbers.PhoneNumber, region: str) -> bool: return phonenumbers.is_carrier_specific_for_region(phone, region)
def is_sms_service(phone: phonenumbers.PhoneNumber, region: str) -> bool: return phonenumbers.is_sms_service_for_region(phone, region)
def normalize_digits(number: str) -> str: return phonenumbers.normalize_digits_only(number)
def normalize_dialable(number: str) -> str: return phonenumbers.normalize_diallable_chars_only(number)
def convert_alpha(number: str) -> str: return phonenumbers.convert_alpha_characters_in_number(number)
def truncate_long(phone: phonenumbers.PhoneNumber) -> bool: return phonenumbers.truncate_too_long_number(phone)
def match_numbers(n1, n2) -> int: return phonenumbers.is_number_match(n1, n2)
def find_numbers(text: str, region: str, leniency=Leniency.VALID) -> list: return list(phonenumbers.PhoneNumberMatcher(text, region, leniency=leniency))
def find_numbers_e164(text: str, region: str) -> list: return [format_e164(m.number) for m in phonenumbers.PhoneNumberMatcher(text, region)]
def as_you_type(region: str) -> phonenumbers.AsYouTypeFormatter: return phonenumbers.AsYouTypeFormatter(region)

def type_name(phone: phonenumbers.PhoneNumber) -> str:
    return {
        PhoneNumberType.FIXED_LINE: "FIXED_LINE",
        PhoneNumberType.MOBILE: "MOBILE",
        PhoneNumberType.FIXED_LINE_OR_MOBILE: "FIXED_LINE_OR_MOBILE",
        PhoneNumberType.TOLL_FREE: "TOLL_FREE",
        PhoneNumberType.PREMIUM_RATE: "PREMIUM_RATE",
        PhoneNumberType.SHARED_COST: "SHARED_COST",
        PhoneNumberType.VOIP: "VOIP",
        PhoneNumberType.PERSONAL_NUMBER: "PERSONAL_NUMBER",
        PhoneNumberType.PAGER: "PAGER",
        PhoneNumberType.UAN: "UAN",
        PhoneNumberType.VOICEMAIL: "VOICEMAIL",
        PhoneNumberType.UNKNOWN: "UNKNOWN",
    }.get(get_number_type(phone), "UNKNOWN")

def info(phone: phonenumbers.PhoneNumber) -> dict:
    return {
        "e164": format_e164(phone),
        "international": format_international(phone),
        "national": format_national(phone),
        "rfc3966": format_rfc3966(phone),
        "country_code": phone.country_code,
        "national_number": phone.national_number,
        "extension": phone.extension,
        "region": get_region(phone),
        "type": type_name(phone),
        "is_valid": is_valid(phone),
        "is_possible": is_possible(phone),
        "is_geographical": is_geographical(phone),
        "is_internationally_dialable": is_internationally_dialable(phone),
        "area_code_length": get_area_code_length(phone),
        "ndc_length": get_ndc_length(phone),
        "national_significant_number": get_national_number(phone),
    }

def parse_safe(number: str, region: str = None) -> phonenumbers.PhoneNumber | None:
    try: return phonenumbers.parse(number, region)
    except NumberParseException: return None