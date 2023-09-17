export default function (isoDate) {
    const date = new Date(isoDate);
    const localDateBR = date.toLocaleDateString('pt-BR');
    return localDateBR;
}
