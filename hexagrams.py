# -*- coding: utf-8 -*-

trigrams = {
    "Ch'ien":   [1, 1, 1],
    "K'un":     [0, 0, 0],
    "K'an":     [0, 1, 0],
    "Chên":     [1, 0, 0],
    "Kên":      [0, 0, 1],
    "Sun":      [0, 1, 1],
    "Tui":      [1, 1, 0],
    "Li":       [1, 0, 1]
}

hexagrams = {
    "Ta Yu":                    trigrams["Ch'ien"] +    trigrams["Li"],
    "Ku":                       trigrams["Sun"] +       trigrams["Kên"],
    "I (Corner of the Mouth)":  trigrams["Chên"] +      trigrams["Tui"],
    "Ta Ch'u":                  trigrams["Ch'ien"] +    trigrams["Kên"],
    "Lü (Treading)":            trigrams["Tui"] +       trigrams["Ch'ien"],
    "Sui":                      trigrams["Chên"] +      trigrams["Tui"],
    "Li":                       trigrams["Li"] +        trigrams["Li"],
    "Shih Ho":                  trigrams["Chên"] +      trigrams["Li"],
    "Lin":                      trigrams["Tui"] +       trigrams["K'un"],
    "Ta Kuo":                   trigrams["Sun"] +       trigrams["Tui"],
    "Mêng":                     trigrams["K'an"] +      trigrams["Kên"],
    "Kuan":                     trigrams["K'un"] +      trigrams["Sun"],
    "P'i":                      trigrams["K'un"] +      trigrams["Ch'ien"],
    "Pi":                       trigrams["Li"] +        trigrams["Kên"],
    "Po":                       trigrams["K'un"] +      trigrams["Kên"],
    "K'un (The Receptive)":     trigrams["K'un"] +      trigrams["K'un"],
    "Shih":                     trigrams["K'an"] +      trigrams["K'un"],
    "Fu":                       trigrams["Chên"] +      trigrams["K'un"],
    "Yü":                       trigrams["K'un"] +      trigrams["Chên"],
    "Chun":                     trigrams["Chên"] +      trigrams["K'an"],
    "Wu Wang":                  trigrams["Chên"] +      trigrams["Ch'ien"],
    "Hsiao Ch'u":               trigrams["Ch'ien"] +    trigrams["Sun"],
    "T'ai":                     trigrams["Ch'ien"] +    trigrams["K'un"],
    "Ch'ien":                   trigrams["Kên"] +       trigrams["K'un"],
    "T'ung Jên":                trigrams["Li"] +        trigrams["Ch'ien"],
    "Hêng":                     trigrams["Sun"] +       trigrams["Chên"],
    "Hsien":                    trigrams["Kên"] +       trigrams["Tui"],
    "Sung":                     trigrams["K'an"] +      trigrams["Ch'ien"],
    "Hsü":                      trigrams["Ch'ien"] +    trigrams["K'an"],
    "K'an":                     trigrams["K'an"] +      trigrams["K'an"],
    "Tun":                      trigrams["Kên"] +       trigrams["Ch'ien"],
    "Ta Chuang":                trigrams["Ch'ien"] +    trigrams["Chên"],
    "Chin":                     trigrams["K'un"] +      trigrams["Li"],
    "Ming I":                   trigrams["Li"] +        trigrams["K'un"],
    "Chia Jên":                 trigrams["Li"] +        trigrams["Sun"],
    "K'uei":                    trigrams["Tui"] +       trigrams["Li"],
    "Chien (Obstruction)":      trigrams["Kên"] +       trigrams["K'an"],
    "Hsieh":                    trigrams["K'an"] +      trigrams["Chên"],
    "Sun (Decrease)":           trigrams["Tui"] +       trigrams["Kên"],
    "I (Increase)":             trigrams["Chên"] +      trigrams["Sun"],
    "Kuai":                     trigrams["Ch'ien"] +    trigrams["Tui"],
    "Kou":                      trigrams["Sun"] +       trigrams["Ch'ien"],
    "Ts'ui":                    trigrams["K'un"] +      trigrams["Tui"],
    "Shêng":                    trigrams["Sun"] +       trigrams["K'un"],
    "K'un (Confining)":         trigrams["K'an"] +      trigrams["Tui"],
    "Ching":                    trigrams["Sun"] +       trigrams["K'an"],
    "Ko":                       trigrams["Li"] +        trigrams["Tui"],
    "Ting":                     trigrams["Sun"] +       trigrams["Li"],
    "Chên":                     trigrams["Chên"] +      trigrams["Chên"],
    "Kên":                      trigrams["Kên"] +       trigrams["Kên"],
    "Chien (Development)":      trigrams["Kên"] +       trigrams["Sun"],
    "Kuei Mei":                 trigrams["Tui"] +       trigrams["Chên"],
    "Fêng":                     trigrams["Li"] +        trigrams["Chên"],
    "Lü (The Wanderer)":        trigrams["Kên"] +       trigrams["Li"],
    "Sun (The Gentle)":         trigrams["Sun"] +       trigrams["Sun"],
    "Tui":                      trigrams["Tui"] +       trigrams["Tui"],
    "Huan":                     trigrams["K'an"] +      trigrams["Sun"],
    "Chieh":                    trigrams["Tui"] +       trigrams["K'an"],
    "Chung Fu":                 trigrams["Tui"] +       trigrams["Sun"],
    "Hsiao Kuo":                trigrams["Kên"] +       trigrams["Chên"],
    "Chi Chi":                  trigrams["Li"] +        trigrams["K'an"],
    "Wei Chi":                  trigrams["K'an"] +      trigrams["Li"]
}
