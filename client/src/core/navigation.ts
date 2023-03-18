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
            icon: "pi pi-fw pi-align-left",
            to: { name: "pdf.word" }
          },
          {
            label: "PDF to Power Point",
            icon: "pi pi-fw pi-align-left",
            to: { name: "pdf.pptx" }
          },
          {
            label: "PDF to JPG",
            icon: "pi pi-fw pi-align-right",
            to: { name: "pdf.jpg" }
          },
          {
            label: "PDF to JPEG",
            icon: "pi pi-fw pi-align-right",
            to: { name: "pdf.jpeg" }
          },
          {
            label: "PDF to PNG",
            icon: "pi pi-fw pi-align-center",
            to: { name: "pdf.png" }
          },
        ],
      },
      {
        label: "Image",
        icon: "pi pi-fw pi-images",
        items: [
          {
            label: "New",
            icon: "pi pi-fw pi-user-plus",
          },
          {
            label: "Delete",
            icon: "pi pi-fw pi-user-minus",
          },
          {
            label: "Search",
            icon: "pi pi-fw pi-users",
            items: [
              {
                label: "Filter",
                icon: "pi pi-fw pi-filter",
                items: [
                  {
                    label: "Print",
                    icon: "pi pi-fw pi-print",
                  },
                ],
              },
              {
                icon: "pi pi-fw pi-bars",
                label: "List",
              },
            ],
          },
        ],
      },
      {
        label: "Word",
        icon: "pi pi-fw pi-file-word",
        items: [
          {
            label: "New",
            icon: "pi pi-fw pi-user-plus",
          },
          {
            label: "Delete",
            icon: "pi pi-fw pi-user-minus",
          },
          {
            label: "Search",
            icon: "pi pi-fw pi-users",
            items: [
              {
                label: "Filter",
                icon: "pi pi-fw pi-filter",
                items: [
                  {
                    label: "Print",
                    icon: "pi pi-fw pi-print",
                  },
                ],
              },
              {
                icon: "pi pi-fw pi-bars",
                label: "List",
              },
            ],
          },
        ],
      },
      {
        label: "Video",
        icon: "pi pi-fw pi-video",
        items: [
          {
            label: "Edit",
            icon: "pi pi-fw pi-pencil",
            items: [
              {
                label: "Save",
                icon: "pi pi-fw pi-calendar-plus",
              },
              {
                label: "Delete",
                icon: "pi pi-fw pi-calendar-minus",
              },
            ],
          },
          {
            label: "Archieve",
            icon: "pi pi-fw pi-calendar-times",
            items: [
              {
                label: "Remove",
                icon: "pi pi-fw pi-calendar-minus",
              },
            ],
          },
        ],
      },
      {
        label: "File",
        icon: "pi pi-fw pi-file",
        items: [
          {
            label: "Edit",
            icon: "pi pi-fw pi-pencil",
            items: [
              {
                label: "Save",
                icon: "pi pi-fw pi-calendar-plus",
              },
              {
                label: "Delete",
                icon: "pi pi-fw pi-calendar-minus",
              },
            ],
          },
          {
            label: "Archieve",
            icon: "pi pi-fw pi-calendar-times",
            items: [
              {
                label: "Remove",
                icon: "pi pi-fw pi-calendar-minus",
              },
            ],
          },
        ],
      },
      {
        label: "Quit",
        icon: "pi pi-fw pi-power-off",
        command: () => {
          alert('Шаряк лох');
        }
      },
    ] 
}