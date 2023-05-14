import type { ITabNavigation } from "@/interfaces/navigation/ITabNavigation";

export function generateTabNavigation(): Array<ITabNavigation> {
  return [
      {
        label: "Home",
        icon: "pi pi-fw pi-home",
        to: { path: '/'}
      },
      {
        label: "PDF",
        icon: "pi pi-fw pi-file-pdf",
        items: [
          {
            label: "PDF to Word",
            icon: "pi pi-fw pi-file",
            to: { name: "pdf.word" }
          },
          {
            label: "PDF to Power Point",
            icon: "pi pi-fw pi-file",
            to: { name: "pdf.pptx" }
          },
          {
            label: "PDF to JPG",
            icon: "pi pi-fw pi-file",
            to: { name: "pdf.jpg" }
          },
          {
            label: "PDF to JPEG",
            icon: "pi pi-fw pi-file",
            to: { name: "pdf.jpeg" }
          },
          {
            label: "PDF to PNG",
            icon: "pi pi-fw pi-file",
            to: { name: "pdf.png" }
          },
        ],
      },
      {
        label: "Word",
        icon: "pi pi-fw pi-file-word",
        items: [
          {
            label: "PDF",
            icon: "pi pi-fw pi-file",
            to: { name: 'word.pdf' }
          },
          {
            label: "TXT",
            icon: "pi pi-fw pi-file",
            to: { name: 'word.txt' }
          }
        ],
      },
      {
        label: "Video",
        icon: "pi pi-fw pi-video",
        items: [
          {
                label: "MP3",
                icon: "pi pi-volume-up",
                to: { name: "mp4.mp3"}
              },
          {
            label: "Compress",
            icon: "pi pi-fw pi-window-minimize",
            to: { name: "mp4.mp4" }
          },
        ],
      },
      {
        label: "File",
        icon: "pi pi-fw pi-file",
        items: [
                    {
            label: "JSON",
            icon: "pi pi-fw pi-file-edit",
            items: [
              {
                label: "CSV",
                icon: "pi pi-fw pi-file-edit",
                to: { name: 'json.csv' }
              },
              {
                label: "XML",
                icon: "pi pi-fw pi-file-edit",
                to: { name: 'json.xml' }
              }
            ],
          },
          {
            label: "XML",
            icon: "pi pi-fw pi-file-edit",
            items: [
              {
                label: "CSV",
                icon: "pi pi-fw pi-file-edit",
                to: { name: 'xml.csv' }
              },
              {
                label: "JSON",
                icon: "pi pi-fw pi-file-edit",
                to: { name: 'xml.json' }
              },
            ],
          },
          {
            label: "CSV",
            icon: "pi pi-fw pi-file-edit",
            items: [
              {
                label: "JSON",
                icon: "pi pi-fw pi-file-edit",
                to: { name: 'csv.json' }
              },
              {
                label: "XML",
                icon: "pi pi-fw pi-file-edit",
                to: { name: 'csv.xml' }
              }
            ],
          },
          {
            label: "HTML",
            icon: "pi pi-fw pi-file-edit",
            items: [
              {
                label: "TXT",
                icon: "pi pi-fw pi-file-edit",
                to: { name: 'html.txt' }
              },
            ],
          }
        ],
      },
    ] 
}