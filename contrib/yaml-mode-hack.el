(require 'yaml-mode)

(defun yaml-extra-highlights ()
  (font-lock-add-keywords 'yaml-mode
   '(;; included files
     ("^\\s-*\\(#\\s-*include\\)\\s-+\\(<[^>]*>\\)"
      (1 font-lock-preprocessor-face prepend)
      (2 font-lock-doc-face prepend))
     ;; variable dollar sign
     ("\\(\\$\\)(" 1 font-lock-keyword-face prepend)
     ;; variable name
     ("\\$(\\([^)$]+\\))" 1 font-lock-function-name-face prepend))))

(add-hook 'yaml-mode-hook 'yaml-extra-highlights)

;;; yaml-mode-hack.el ends here
