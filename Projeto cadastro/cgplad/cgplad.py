class Usuario:
    def __int__(self, id_usuario, nome, email, perfil="Comum"):
        self.id_usuario = id_usuario
        self.nome  = nome
        self.email = email
        self.perfil = perfil

    def __str__(self):
        return f"[{self.id_usuario}] {self.nome} - {self.email} - {self.perfil}"
    