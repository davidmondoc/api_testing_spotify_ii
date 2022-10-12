from requests_folder.albums.get_album import get_album

class TestAlbums:
    '''
    testare functionala (functional testing) = tip de testare in care se verifica daca sistemul  isi indeplineste functiile
                                             = se cosnidera a fi testare blackbox
                                             = se baseaza pe cerintele de business

    testare non-functionala (non-functional testing) = este un tip de testare care verifica cat de bine isi indeplineste sistemul funtiile
    1. Performance testing
- stress testing = tip de testare in care se verifica comportamentul sistemului atunci cand este incarcat aproape de limita superioara
- load testing = tip de testare in care se verifica comportamentul sistemului la un nivel specific de incarcare de utilizatori (spre exemplu atunci cand estimam o anumita crestere a numarului de utilizatori in urma lansarii unei noi functionalitati)
- volume testing = tip de testare in care se verifica comportamentul sistemului la un nivel specific de incarcare de date (spre exemplu atunci cand estimam o anumita crestere a numarului de date in urma fuziunii cu o alta companie de la care preluam baza de date)
- spike testing = tip de testare care verfica comportamentul sistemului la o crestere brusca a numarului de utilizatori sau de date
- scalability testing = tip de testare care verifica comportamentul sistemului la o crestere progresiva de utilizatori sau de date

2. Recovery testing = tip de testare care verifica in ce masura sistemul isi revine dupa un crash
3. Compatibility testing = verifica compatibilitatea sistemului cu mai multe platforme (ex:mai multe browsere, mai multe sisteme de operare)
4. Portability testing = verifica posibilitatea de a muta produsul de pe un sistem pe celalt (ex: de pe windows pe linux)
5. Localisation testing = verifica comportamentul sistemului din punctul de vedere al locatiei in care il folosim (ex: sa suporte accente frantuzesti sau spaniole sau caractere chinezesti / japoneze)
6. Mentenability testing = tip de testare in care verificam posibilitatea mentenantei, adica a modificarilor aduse aplicatiei fara a impacta prea mult alte zone din aplicatie
7. Usability testing = tip de testare care verifica cat de buna este experienta utilizatorului cu aplicatia (vizual daca este placut, daca este intuitiv, usor de folosit etc)
8. Accessibility testing = tip de testare care verifica usurinta de folosire a aplicatiei pentru persoane cu dizabilitati
    '''
    # @functionaltesting    @positivetesting
    def test_get_album_exists(self):
        response=get_album('1mc8M9eR9ZIBxqWA2CA4Wo')
        assert response.status_code == 200

    # @functionaltesting    @negativetesting
    def test_get_album_does_not_exist(self):
        response=get_album('1mc8M9eR9ZIBxqWA2CA4WN')
        assert response.status_code == 404

# @functionaltesting @negativetesting
    def test_get_album_invalid(self):
        response=get_album('*mc8M9eR9ZIBxqWA2CA4WN&')
        print(response.reason)
        assert response.status_code == 400