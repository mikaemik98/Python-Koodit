kuukaudet = ("tammikuu", "helmikuu", "maaliskuu", "huhtikuu", "toukokuu", "kesäkuu", "heinäkuu", "elokuu", "syyskuu", "lokakuu", "marraskuu", "joulukuu")
vuodenajat = {"tammikuu": "talvi", "helmikuu": "talvi", "maaliskuu": "kevät", "huhtikuu": "kevät", "toukokuu": "kevät", "kesäkuu": "kesä", "heinäkuu": "kesä", "elokuu": "kesä", "syyskuu": "syksy", "lokakuu": "syksy", "marraskuu": "syksy", "joulukuu": "talvi"}
järjestysnumero = int(input('Anna kuukauden numero (1-12): '))
kuukausi = kuukaudet[järjestysnumero - 1]
if kuukausi in vuodenajat:
    print(f'{kuukausi} on {vuodenajat[kuukausi]} kuukausi')
