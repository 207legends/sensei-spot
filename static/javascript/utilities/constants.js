const CONSTANTS = {
    OFFER_OF_DAY: {
        STATE: false,
    },
    REGEX: {
        EMAIL: /^[a-zA-Z0-9._%-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/,
        PASSWORD: /(?=^.{8,}$)((?=.*[A-Za-z0-9])(?=.*[A-Z])(?=.*[a-z]))^.*/,
        CREDIT_CARD: /^(?:4[0-9]{12}(?:[0-9]{3})?|5[1-5][0-9]{14}|6011[0-9]{12}|3(?:0[0-5]|[68][0-9])[0-9]{11}|3[47][0-9]{13})$/,
        ALPHABET_ONLY: /^[a-zA-Z]+$/,
        ALPHANUMERIC: /^[a-zA-Z0-9]+$/,
    }
}


